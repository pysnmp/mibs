#
# PySNMP MIB module TWOWCOM-SMI (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/2wcom/TWOWCOM-SMI
# Produced by pysmi-1.1.12 at Tue Sep 17 11:58:48 2024
# On host fv-az888-540 platform Linux version 6.8.0-1014-azure by user runner
# Using Python version 3.10.15 (main, Sep  9 2024, 03:02:45) [GCC 11.4.0]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ConstraintsIntersection, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ConstraintsIntersection", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Integer32, MibIdentifier, TimeTicks, Gauge32, ObjectIdentity, Counter64, Counter32, Bits, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, IpAddress, enterprises, iso, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "MibIdentifier", "TimeTicks", "Gauge32", "ObjectIdentity", "Counter64", "Counter32", "Bits", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "IpAddress", "enterprises", "iso", "ModuleIdentity")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
twowcom = ModuleIdentity((1, 3, 6, 1, 4, 1, 21529))
twowcom.setRevisions(('2011-06-23 12:00', '2009-04-27 14:25', '2008-02-19 10:37', '2006-10-26 16:04', '2006-06-01 11:51',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: twowcom.setRevisionsDescriptions(('Version V0.5\r\n\t\t\t\t- new object tree dvbMultiplexer (1.3.6.1.4.1.21529.3.3)', 'Version V0.4\r\n\t\t\t\t- new object tree generator (1.3.6.1.4.1.21529.4)', 'Version V0.3\r\n\t\t\t\t- new object tree dvb (1.3.6.1.4.1.21529.3)', 'Version V0.2\r\n\t\t\t\t- all textual conventions moved to the TWOWCOM-COMMONVARBINS Mib.\r\n\t\t\t\t', 'Version V0.1',))
if mibBuilder.loadTexts: twowcom.setLastUpdated('201106231200Z')
if mibBuilder.loadTexts: twowcom.setOrganization('2wcom GmbH')
if mibBuilder.loadTexts: twowcom.setContactInfo('2wcom GmbH\r\n\t\t\t\tc/o Martin Hoppe\r\n\t\t\t\tLise-Meitner-Str. 4\r\n\t\t\t\t24941 Flensburg\r\n\t\t\t\tGermany\r\n\t\t\t\t\t\t\t\t\r\n\t\t\t\tTel: +49 461 662830-35\r\n\t\t\t\tFax: +49 461 662830-11\r\n\t\t\t\t\t\t\t\t\r\n\t\t\t\tWEB: www.2wcom.com\r\n\t\t\t\t')
if mibBuilder.loadTexts: twowcom.setDescription('2wcom MIB Modul')
encoder = MibIdentifier((1, 3, 6, 1, 4, 1, 21529, 1))
decoder = MibIdentifier((1, 3, 6, 1, 4, 1, 21529, 2))
dvb = MibIdentifier((1, 3, 6, 1, 4, 1, 21529, 3))
dvbEncoder = MibIdentifier((1, 3, 6, 1, 4, 1, 21529, 3, 1))
dvbDecoder = MibIdentifier((1, 3, 6, 1, 4, 1, 21529, 3, 2))
dvbMultiplexer = MibIdentifier((1, 3, 6, 1, 4, 1, 21529, 3, 3))
generator = MibIdentifier((1, 3, 6, 1, 4, 1, 21529, 4))
other = MibIdentifier((1, 3, 6, 1, 4, 1, 21529, 10))
mibBuilder.exportSymbols("TWOWCOM-SMI", decoder=decoder, dvbDecoder=dvbDecoder, dvb=dvb, encoder=encoder, dvbMultiplexer=dvbMultiplexer, other=other, PYSNMP_MODULE_ID=twowcom, twowcom=twowcom, dvbEncoder=dvbEncoder, generator=generator)

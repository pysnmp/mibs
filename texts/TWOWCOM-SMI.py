#
# PySNMP MIB module TWOWCOM-SMI (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/2wcom/TWOWCOM-SMI
# Produced by pysmi-1.1.12 at Tue Jun  4 12:17:27 2024
# On host fv-az1789-327 platform Linux version 6.5.0-1021-azure by user runner
# Using Python version 3.10.14 (main, May  8 2024, 15:05:35) [GCC 11.4.0]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueRangeConstraint, ValueSizeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueRangeConstraint", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsUnion")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
NotificationType, iso, Bits, Integer32, enterprises, Counter32, Gauge32, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, Unsigned32, ModuleIdentity, MibIdentifier, Counter64, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "iso", "Bits", "Integer32", "enterprises", "Counter32", "Gauge32", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "Unsigned32", "ModuleIdentity", "MibIdentifier", "Counter64", "TimeTicks")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
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
mibBuilder.exportSymbols("TWOWCOM-SMI", twowcom=twowcom, generator=generator, other=other, dvb=dvb, dvbEncoder=dvbEncoder, PYSNMP_MODULE_ID=twowcom, encoder=encoder, decoder=decoder, dvbDecoder=dvbDecoder, dvbMultiplexer=dvbMultiplexer)

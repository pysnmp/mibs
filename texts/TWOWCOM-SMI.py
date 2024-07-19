#
# PySNMP MIB module TWOWCOM-SMI (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/2wcom/TWOWCOM-SMI
# Produced by pysmi-1.1.12 at Fri Jul 19 10:01:03 2024
# On host fv-az1771-969 platform Linux version 6.5.0-1023-azure by user runner
# Using Python version 3.10.14 (main, Jun 20 2024, 15:20:03) [GCC 11.4.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ValueSizeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Bits, Integer32, Counter64, Gauge32, ModuleIdentity, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, TimeTicks, enterprises, Counter32, ObjectIdentity, Unsigned32, iso, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Integer32", "Counter64", "Gauge32", "ModuleIdentity", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "TimeTicks", "enterprises", "Counter32", "ObjectIdentity", "Unsigned32", "iso", "NotificationType")
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
mibBuilder.exportSymbols("TWOWCOM-SMI", dvbMultiplexer=dvbMultiplexer, dvb=dvb, twowcom=twowcom, PYSNMP_MODULE_ID=twowcom, decoder=decoder, generator=generator, dvbEncoder=dvbEncoder, other=other, dvbDecoder=dvbDecoder, encoder=encoder)

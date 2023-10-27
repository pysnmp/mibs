#
# PySNMP MIB module TWOWCOM-SMI (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/2wcom/TWOWCOM-SMI
# Produced by pysmi-1.1.10 at Fri Oct 27 07:34:30 2023
# On host fv-az1236-588 platform Linux version 6.2.0-1015-azure by user runner
# Using Python version 3.10.13 (main, Aug 28 2023, 08:28:42) [GCC 11.4.0]
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsIntersection")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, Counter64, Gauge32, TimeTicks, enterprises, iso, IpAddress, MibIdentifier, Integer32, ModuleIdentity, Unsigned32, ObjectIdentity, NotificationType, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "Counter64", "Gauge32", "TimeTicks", "enterprises", "iso", "IpAddress", "MibIdentifier", "Integer32", "ModuleIdentity", "Unsigned32", "ObjectIdentity", "NotificationType", "Counter32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
twowcom = ModuleIdentity((1, 3, 6, 1, 4, 1, 21529))
twowcom.setRevisions(('2011-06-23 12:00', '2009-04-27 14:25', '2008-02-19 10:37', '2006-10-26 16:04', '2006-06-01 11:51',))
if mibBuilder.loadTexts: twowcom.setLastUpdated('201106231200Z')
if mibBuilder.loadTexts: twowcom.setOrganization('2wcom GmbH')
encoder = MibIdentifier((1, 3, 6, 1, 4, 1, 21529, 1))
decoder = MibIdentifier((1, 3, 6, 1, 4, 1, 21529, 2))
dvb = MibIdentifier((1, 3, 6, 1, 4, 1, 21529, 3))
dvbEncoder = MibIdentifier((1, 3, 6, 1, 4, 1, 21529, 3, 1))
dvbDecoder = MibIdentifier((1, 3, 6, 1, 4, 1, 21529, 3, 2))
dvbMultiplexer = MibIdentifier((1, 3, 6, 1, 4, 1, 21529, 3, 3))
generator = MibIdentifier((1, 3, 6, 1, 4, 1, 21529, 4))
other = MibIdentifier((1, 3, 6, 1, 4, 1, 21529, 10))
mibBuilder.exportSymbols("TWOWCOM-SMI", encoder=encoder, dvbMultiplexer=dvbMultiplexer, dvbDecoder=dvbDecoder, generator=generator, PYSNMP_MODULE_ID=twowcom, dvbEncoder=dvbEncoder, other=other, decoder=decoder, twowcom=twowcom, dvb=dvb)

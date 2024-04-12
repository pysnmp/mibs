#
# PySNMP MIB module TWOWCOM-SMI (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/2wcom/TWOWCOM-SMI
# Produced by pysmi-1.1.12 at Fri Apr 12 00:24:03 2024
# On host fv-az975-788 platform Linux version 6.5.0-1017-azure by user runner
# Using Python version 3.10.14 (main, Mar 20 2024, 15:15:25) [GCC 11.4.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
TimeTicks, Counter32, Bits, Unsigned32, Integer32, IpAddress, ModuleIdentity, NotificationType, MibIdentifier, Gauge32, enterprises, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, iso, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "Counter32", "Bits", "Unsigned32", "Integer32", "IpAddress", "ModuleIdentity", "NotificationType", "MibIdentifier", "Gauge32", "enterprises", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "iso", "Counter64")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
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
mibBuilder.exportSymbols("TWOWCOM-SMI", other=other, dvb=dvb, twowcom=twowcom, dvbEncoder=dvbEncoder, dvbDecoder=dvbDecoder, dvbMultiplexer=dvbMultiplexer, decoder=decoder, PYSNMP_MODULE_ID=twowcom, encoder=encoder, generator=generator)

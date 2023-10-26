#
# PySNMP MIB module BLUECATNETWORKS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/bluecatnetworks/BLUECATNETWORKS-MIB
# Produced by pysmi-1.1.8 at Thu Oct 26 12:08:10 2023
# On host fv-az1234-823 platform Linux version 6.2.0-1015-azure by user runner
# Using Python version 3.10.13 (main, Aug 28 2023, 08:28:42) [GCC 11.4.0]
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsUnion, ConstraintsIntersection, SingleValueConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "SingleValueConstraint", "ValueRangeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Integer32, Unsigned32, Counter64, iso, Gauge32, Counter32, enterprises, ModuleIdentity, TimeTicks, Bits, IpAddress, ObjectIdentity, MibIdentifier, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "Unsigned32", "Counter64", "iso", "Gauge32", "Counter32", "enterprises", "ModuleIdentity", "TimeTicks", "Bits", "IpAddress", "ObjectIdentity", "MibIdentifier", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
bluecatnetworksId = ModuleIdentity((1, 3, 6, 1, 4, 1, 13315, 1))
bluecatnetworksId.setRevisions(('2010-11-30 00:00',))
if mibBuilder.loadTexts: bluecatnetworksId.setLastUpdated('201011300000Z')
if mibBuilder.loadTexts: bluecatnetworksId.setOrganization('BlueCat Networks Inc.')
bluecatnetworks = MibIdentifier((1, 3, 6, 1, 4, 1, 13315))
appliances = MibIdentifier((1, 3, 6, 1, 4, 1, 13315, 100))
mibBuilder.exportSymbols("BLUECATNETWORKS-MIB", bluecatnetworks=bluecatnetworks, bluecatnetworksId=bluecatnetworksId, appliances=appliances, PYSNMP_MODULE_ID=bluecatnetworksId)

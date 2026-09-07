#
# PySNMP MIB module CISCO-GYROAC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source CISCO-GYROAC-MIB
# Source digest sha256:4cb2522bf283aa75bb8995f9260804219c682c173e0cca7b49d792bcf57ebc61
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoGyroacMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 859))
ciscoGyroacMIB.setRevisions(('2019-01-09 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoGyroacMIB.setRevisionsDescriptions(('Latest version of this MIB module.',))
if mibBuilder.loadTexts: ciscoGyroacMIB.setLastUpdated('2019-01-09 00:00')
if mibBuilder.loadTexts: ciscoGyroacMIB.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoGyroacMIB.setContactInfo('Cisco Systems\n            Customer Service\n\n            Postal: 170 W Tasman Drive\n            San Jose, CA  95134\n            USA\n\n            Tel: +1 800 553-NETS\n\n            E-mail: cs-ir800@cisco.com')
if mibBuilder.loadTexts: ciscoGyroacMIB.setDescription('This MIB module defines management objects for monitoring of\n        Gyroscope andvAccelerometer for IR8x9 routers.\n\n        Gyroscope feature provides information about Gyroscope data\n        shows G-X, Y, Z (3D gyroscope data) in mdps (milli Degrees Per\n        Second) and accelerometer feature provides information        \n        about XL-X, Y, Z (3D accelerator data) in unit\n        mg(milligram).\n\n        Accelerometer and Gyroscope functionality tracks the speed and\n        angular movement of the device.\n\n        *** ABBREVIATIONS, ACRONYMS, AND SYMBOLS ***\n\n        gyro - Gyroscope sensor of IR8x9 routers')
ciscoGyroacMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 859, 0))
ciscoGyro = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 859, 0, 1), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ciscoGyro.setStatus('current')
if mibBuilder.loadTexts: ciscoGyro.setDescription('An entry containing the management information for a particular\n        sensor gyroscope and accelerometer')
mibBuilder.exportSymbols("CISCO-GYROAC-MIB", PYSNMP_MODULE_ID=ciscoGyroacMIB, ciscoGyro=ciscoGyro, ciscoGyroacMIB=ciscoGyroacMIB, ciscoGyroacMIBObjects=ciscoGyroacMIBObjects)
